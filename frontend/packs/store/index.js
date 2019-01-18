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
        jails: {}
    },
    mutations: {
        [types.RELOAD_JAILS](state, jails) {
            state.jails = jails
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
        }
    }
})