import Vue from 'vue'
import Vuex from 'vuex'
import * as types from './mutation-types.js'

Vue.use(Vuex)
import axios from 'axios'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export const store = new Vuex.Store({
    state: {
        serverName: 'http://localhost',
        jails: {},
        fetched_releases: [],
        non_fetch_releases: [],
        loading: false
    },
    mutations: {
        [types.RELOAD_JAILS](state, jails) {
            state.jails = jails
        },
        [types.RELOAD_RELEASES](state, releases_array) {
            state.fetched_releases = releases_array.fetched_releases
            state.non_fetch_releases = releases_array.non_fetch_releases
        }
    },
    actions: {
        async reload_jails(context) {
            let jails = {};
            await axios.get(this.state.serverName + '/jails/fetch_jails', {})
                .then(response => {
                    console.log(response)
                    jails = response.data
                });
            context.commit(types.RELOAD_JAILS, jails);
        },
        async reload_releases(context) {
            let fetched_releases = [];
            let non_fetch_releases = [];
            await axios.get(this.state.serverName + '/jails/fetch_releases', {})
                .then(response => {
                    let json_response = []
                    json_response = response.data
                    let len = response.data.length
                    for (let i = 0; i < len; i++) {
                        if (json_response[i].fetched) {
                            fetched_releases.push(json_response[i].name)
                        } else {
                            non_fetch_releases.push(json_response[i].name)
                        }
                    }
                });
            context.commit(types.RELOAD_RELEASES, { fetched_releases: fetched_releases, non_fetch_releases: non_fetch_releases });
        }
    }
})