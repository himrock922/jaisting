<template>
  <b-form-group label="Fetch Relase">
    <b-form-select v-model="fetching_release_selected" :options="$store.state.non_fetch_releases" class="mb-3"/>
    <div>Selected: <strong>{{ fetching_release_selected }}</strong></div>
    <button type="button" class="btn btn-success" @click="release_download">DL</button>
  </b-form-group>
</template>

<script>
    import axios from 'axios'

    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    export default {
        name: 'Fetch-Release',
        data() {
            return {
                fetching_release_selected: null
            }
        },
        props: {
            jail_name: String
        },
        methods: {
            release_download: function () {
                this.$store.state.loading = true
                axios.post(this.$store.state.serverName + '/jails/release_download', {
                    release: this.fetching_release_selected
                })
                    .then(response => {
                        this.$store.dispatch('reload_releases')
                        this.$store.state.loading = false
                    })
                    .catch(error => {
                        alert(error.response.data)
                        this.$store.state.loading = false
                    })
            }
        }
    }
</script>

<style scoped>

</style>