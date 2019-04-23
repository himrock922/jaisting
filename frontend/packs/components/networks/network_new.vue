<template>

  <div v-if="$store.state.loading">
    <vue-loading type="spin" :size="{ width: '150px', height: '150px' }"></vue-loading>
  </div>
  <div v-else-if="!$store.state.loading">
    <div>
      <b-modal v-model="showDialog">
        <h3>network configured.</h3>
        <p>jail_name: {{ config.id }}</p>
        <p>interfaces: {{ config.interfaces }}</p>
        <p>ipv4_addr: {{ config.ip4_addr }}</p>
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
                showDialog: false,
                config: {}
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
                        this.config = response.data.jail_config
                        this.showDialog = true
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