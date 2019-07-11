<template>
  <div v-if="$store.state.loading">
    <vue-loading type="spin" :size="{ width: '150px', height: '150px' }"></vue-loading>
  </div>
  <div v-else-if="!$store.state.loading">
    <b-button variant="success" id="ipfw-add" @click="toggleModal">Add</b-button>
    <b-modal ref="my-modal" hide-footer title="add chain">
      <b-button class="mt-2" variant="outline-warning" block @click="toggleModal">Toggle Me</b-button>
    </b-modal>
    <table class="table table-striped table-sm">
      <thead>
      <tr>
        <th>Rule Number</th>
        <th>Rule Format</th>
        <th>Protocol Target</th>
        <th></th>
        <th>From Target</th>
        <th></th>
        <th>To Target</th>
      </tr>
      </thead>
      <tbody id="app">
      <tr v-for="(list, index) in this.firewall_lists">
          <td>{{ list[0] }}</td>
          <td>{{ list[1] }}</td>
          <td>{{ list[2] }}</td>
          <td>{{ list[3] }}</td>
          <td>{{ list[4] }}</td>
          <td>{{ list[5] }}</td>
          <td>{{ list[6] }}</td>
          <td>{{ list[7] }}</td>
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
        data: function() {
          return {
            firewall_lists: []
          }
        },
        components: {
            'vue-loading': VueLoading
        },
        methods: {
          toggleModal() {
            this.$refs['my-modal'].toggle('#ipfw-add')
          }
        },
        async mounted() {
            await this.$store.dispatch('reload_firewall')
            let flatten_array = this.$store.state.firewall_lists

            for(var i = 0; i < flatten_array.length; i++) {
              let firewall_rule = flatten_array[i].split(/\s/)
              let style_range;
              let generater_firewall_rule = [];
              firewall_rule.map(function(value, index) {
                if(value === 'from') {
                  generater_firewall_rule.push(style_range);
                  style_range = "";
                  generater_firewall_rule.push(firewall_rule[index]);
                }
                if(value === 'to') {
                  generater_firewall_rule.push(style_range.slice(6));
                  style_range = "";
                  generater_firewall_rule.push(firewall_rule[index]);
                }
                style_range += " " + value;
                if(index === 0 || index === 1) {
                  generater_firewall_rule.push(firewall_rule[index]);
                  style_range = "";
                }
              });
              generater_firewall_rule.push(style_range.slice(4));
              this.firewall_lists.push(generater_firewall_rule);
            }
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