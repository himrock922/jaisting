<template>
  <div v-if="$store.state.loading">
    <vue-loading type="spin" :size="{ width: '150px', height: '150px' }"></vue-loading>
  </div>
  <div v-else-if="!$store.state.loading">
    <table class="table table-striped table-sm">
      <thead>
      <tr>
        <th>All Results</th>
      </tr>
      </thead>
      <tbody id="app">
      <tr v-for=" list in $store.state.firewall_lists">
          <td>{{ list }}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
    import axios from 'axios'
    import {VueLoading} from 'vue-loading-template'

    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    export default {
        name: 'Firewall-Index',
        components: {
            'vue-loading': VueLoading
        },
        mounted: function () {
            this.$store.dispatch('reload_firewall')
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