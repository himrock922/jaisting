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
                axios.delete(this.$store.state.serverName + '/jails/delete', {
                    data: { jail_name: this.jail_name }
                })
                    .then(response => {
                        console.log(response)
                        this.$store.dispatch('reload_jails')
                    })
                    .catch(error => {
                        alert(error.response.data)
                    })
            }
        }
    }
</script>

<style scoped>

</style>