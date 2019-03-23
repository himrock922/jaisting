<template>
  <button type="button" class="btn btn-danger" @click="jail_delete">DELETE</button>
</template>

<script>
    import axios from 'axios'

    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    export default {
        name: 'Jail-Delete',
        props: {
            jail_name: String
        },
        methods: {
            jail_delete: function () {
                this.$store.state.loading = true
                axios.delete(this.$store.state.serverName + '/jails/delete', {
                    data: { jail_name: this.jail_name }
                })
                    .then(response => {
                        this.$store.dispatch('reload_jails')
                        this.$store.state.loading = false
                    })
                    .catch(error => {
                        alert(error.response.data.reason)
                        this.$store.state.loading = false
                    })
            }
        }
    }
</script>

<style scoped>

</style>