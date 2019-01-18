<template>
  <button type="button" class="btn btn-warning" @click="jail_stop">Stop</button>
</template>

<script>
    import axios from 'axios'

    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    export default {
        name: 'Jail-Stop',
        props: {
            jail_name: String
        },
        methods: {
            jail_stop: function () {
                axios.put(this.$store.state.serverName + '/jails/stop', {
                    jail_name: this.jail_name
                })
                    .then(response => {
                        console.log(response)
                        this.$store.dispatch('reload_jails')
                    })
                    .catch(error => {
                        alert(error.response)
                    })
            }
        }
    }
</script>

<style scoped>

</style>