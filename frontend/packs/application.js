import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import '../css/application.css'
import '../css/login.css'
import '../css/dashboard.css'
import '../css/top.css'
import 'xterm/css/xterm.css'
import { store } from './store/index'
import FirewallIndex from './components/firewall/index.vue'
import JailsIndex from './components/jails_index.vue'
import JailNew from './components/jail_new.vue'
import JailConnect from './components/jail_connect.vue'
import NetworkNew from './components/networks/network_new.vue'
import Vue from 'vue'
import BootstrapVue from "bootstrap-vue";
Vue.use(BootstrapVue);

document.addEventListener("DOMContentLoaded", function (event) {
    if (document.getElementById("app") != null) {
        new Vue({
            el: '#app',
            store,
            components: {
                'jails-index': JailsIndex,
                'jail-new': JailNew,
                'jail-connect': JailConnect,
                'network-new': NetworkNew,
                'firewall-index' : FirewallIndex,
            }
        })
    }
})