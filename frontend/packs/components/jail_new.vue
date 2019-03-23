<template>
  <div v-if="$store.state.loading">
    <vue-loading type="spin" :size="{ width: '150px', height: '150px' }"></vue-loading>
  </div>
  <div v-else-if="!$store.state.loading">
    <h2>Jail New</h2>
    <b-form-group label="Create Jail System">
      <b-form-input v-model="input_name"
                    type="text"
                    placeholder="Please Input of jail name"></b-form-input>
      <p>Value: {{ input_name }}</p>
      <b-form-select v-model="selected" :options="$store.state.fetched_releases" class="mb-3"/>
      <div>Selected: <strong>{{ selected }}</strong></div>
      <button type="button" class="btn btn-success" @click="jail_create">Create</button>
    </b-form-group>
    <fetch-release></fetch-release>
  </div>
</template>

<script>
    import axios from 'axios'
    import FetchRelease from './fetch_release.vue'
    import {VueLoading} from 'vue-loading-template'

    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    export default {
        name: 'Jail-New',
        data() {
            return {
                input_name: '',
                selected: null,
            }
        },
        components: {
            'fetch-release': FetchRelease,
            'vue-loading': VueLoading
        },
        props: {
            jail_name: String,
            release: String
        },
        methods: {
            jail_create: function () {
                this.$store.state.loading = true
                axios.post(this.$store.state.serverName + '/jails/create', {
                    jail_name: this.input_name,
                    release: this.selected
                })
                    .then(response => {
                        this.$store.state.loading = false
                    })
                    .catch(error => {
                        this.$store.state.loading = false
                        alert(error.response.data.reason)
                    })
            }
        },
        created: function () {
            this.$store.dispatch('reload_releases')
        }
    }
</script>

<style scoped>
  .vue-loading {
    color: #0DC5C1;
    position: absolute;
    top: 50%;
    left: 50%;
    margin-left: -75x;
    margin-top: 150px;
    overflow: auto;
  }
</style>