<template>
  <button type="button" class="btn btn-success" @click="jail_start">Start</button>
</template>

<script>
    import axios from 'axios'

    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    export default {
        name: 'Jail-Start',
        props: {
            jail_name: String
        },
        methods: {
            jail_start: function () {
                this.$store.state.loading = true
                axios.put(this.$store.state.serverName + '/jails/start', {
                    jail_name: this.jail_name
                })
                    .then(response => {
                        this.$store.dispatch('reload_jails')
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