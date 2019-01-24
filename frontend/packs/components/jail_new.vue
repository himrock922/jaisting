<template>
  <div>
    <b-form-input v-model="input_name"
                  type="text"
                  placeholder="Please Input of jail name"></b-form-input>
    <p>Value: {{ input_name }}</p>
    <b-form-select v-model="selected" :options="fetched_releases" class="mb-3"/>
    <div>Selected: <strong>{{ selected }}</strong></div>
    <button type="button" class="btn btn-success" @click="jail_create">Create</button>
  </div>
</template>

<script>
    import axios from 'axios'

    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    export default {
        name: 'Jail-New',
        data() {
            return {
                input_name: '',
                selected: null,
                fetched_releases: []
            }
        },
        props: {
            jail_name: String,
            release: String
        },
        methods: {
            fetch_releases: function () {
                axios.get(this.$store.state.serverName + '/jails/fetch_releases', {})
                    .then(response => {
                        let json_response = []
                        json_response = response.data
                        let len = response.data.length
                        for (let i=0; i< len; i++) {
                            if(json_response[i].fetched) {
                                this.fetched_releases.push(json_response[i].name)
                            }
                        }
                    })
            },
            jail_create: function () {
                axios.post(this.$store.state.serverName + '/jails/create', {
                    jail_name: this.input_name,
                    release: this.selected
                })
                    .then(response => {
                        console.log(response)
                    })
                    .catch(error => {
                        alert(error.response)
                    })
            }
        },
        created: function () {
            this.fetch_releases()
        }
    }
</script>

<style scoped>

</style>