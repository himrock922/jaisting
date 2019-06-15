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
        firewalls: [],
        jail_names: {},
        fetched_releases: [],
        non_fetch_releases: [],
        loading: false
    },
    mutations: {
        [types.FETCH_JAILS](state, jail_names) {
            state.jail_names = jail_names
        },
        [types.RELOAD_FIREWALLS](state, firewalls) {
            state.firewalls = firewalls
        },
        [types.RELOAD_JAILS](state, jails) {
            state.jails = jails
        },
        [types.RELOAD_RELEASES](state, releases_array) {
            state.fetched_releases = releases_array.fetched_releases
            state.non_fetch_releases = releases_array.non_fetch_releases
        }
    },
    actions: {
        async fetch_jails(context) {
            let jail_names = [];
            await axios.get(this.state.serverName + '/networks/get_jails', {})
                .then(response => {
                    console.log(response)
                    let json_response = []
                    json_response = response.data
                    let len = response.data.length
                    for (let i = 0; i < len; i++) {
                        jail_names.push(json_response[i].name)
                    }
                });
            context.commit(types.FETCH_JAILS, jail_names);
        },
        async reload_firewalls(context) {
            let firewalls = [];
            await axios.get(this.state.serverName + '/firewalls/fetch_all_lists', {})
                .then(response => {
                    let json_response = []
                    json_response = response.data.firewall_lists
                    let len = response.data.firewall_lists.length
                    for (let i = 0; i < len; i++) {
                        firewalls.push(json_response[i])
                    }
                });
            context.commit(types.RELOAD_FIREWALLS, firewalls);
        },
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
            context.commit(types.RELOAD_RELEASES, {
                fetched_releases: fetched_releases,
                non_fetch_releases: non_fetch_releases
            });
        }
    }
})
