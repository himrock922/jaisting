<template>

  <div v-if="$store.state.loading">
    <vue-loading type="spin" :size="{ width: '150px', height: '150px' }"></vue-loading>
  </div>
  <div v-else-if="!$store.state.loading">
    <div>
      <b-modal v-model="showModal">
        <h3>Sample Config</h3>
        <p v-for="command in commands_created">
          {{ command }}
        </p>
        <p v-for="command in commands_start">
          {{ command }}
        </p>
      </b-modal>
    </div>
    <b-form-group label="Create Network">

      <b-form-input v-model="bridge_name"
                    type="text"
                    placeholder="Please Input of Brdige Interface Name to associate jail"></b-form-input>
      <p>Value: {{ bridge_name }}</p>
      <b-form-select v-model="selected" :options="$store.state.jail_names" class="mb-3"/>
      <div>Selected: <strong>{{ selected }}</strong></div>
      <b-form-input v-model="interfaces"
                    type="text"
                    placeholder="Please Input of Interface Name to associate jail"></b-form-input>
      <p>Value: {{ interfaces }}</p>
      <b-form-input v-model="ipv4_addresses"
                    type="text"
                    placeholder="Please Input of IPv4 address to associate jail"></b-form-input>
      <p>Value: {{ ipv4_addresses }}</p>
      <button type="button" class="btn btn-success" @click="network_create">Create</button>
    </b-form-group>
  </div>
</template>

<script>
    import axios from 'axios'
    import {VueLoading} from 'vue-loading-template'

    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    export default {
        name: 'Network-New',
        data() {
            return {
                selected: null,
                bridge_name: '',
                ipv4_addresses: '',
                interfaces: '',
                commands_created: [],
                commands_start: [],
                showModal: false
            }
        },
        components: {
            'vue-loading': VueLoading
        },
        methods: {
            network_create: function () {
                this.$store.state.loading = true
                axios.post(this.$store.state.serverName + '/networks/create', {
                    bridge_name: this.bridge_name,
                    ipv4_addresses: this.ipv4_addresses,
                    interfaces: this.interfaces,
                    jail_name: this.selected
                })
                    .then(response => {
                        this.$store.state.loading = false
                        let commands_created = response.data.commands_created
                        let commands = []
                        let commands2 = []
                        let len = response.data.commands_created.length
                        for (let i = 0; i < len; i++) {
                            commands.push(commands_created[i])
                        }
                        this.commands_created = commands
                        let commands_start = response.data.commands_start
                        let len2 = response.data.commands_start.length
                        for (let i = 0; i < len2; i++) {
                            commands2.push(commands_start[i])
                        }
                        this.commands_start = commands2
                        this.showModal = true
                    })
                    .catch(error => {
                        this.$store.state.loading = false
                        alert(error.response.data.reason)
                    })
            }
        },
        created: function () {
            this.$store.dispatch('fetch_jails')
        }
    }
</script>

<style scoped>
  .vue-loading {
    color: #0DC5C1;
    position: absolute;
    top: 50%;
    left: 50%;
    margin-left: -150x;
    margin-top: 150px;
    overflow: auto;
  }
</style>