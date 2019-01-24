import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import '../css/application.css'
import '../css/login.css'
import '../css/top.css'
import { store } from './store/index'
import JailsIndex from './components/jails_index.vue'
import JailNew from './components/jail_new.vue'
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
            }
        })
    }
})