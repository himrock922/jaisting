<template>
  <div v-if="$store.state.loading">
    <vue-loading type="spin" :size="{ width: '150px', height: '150px' }"></vue-loading>
  </div>
  <div v-else-if="!$store.state.loading">
    <b-button variant="success" id="ipfw-add" @click="ipfw_add">Add</b-button>
    <b-modal ref="add_button" hide-footer title="add chain" size="xl">
      <p v-if="errors.length">
        <b>Please correct the following error(s):</b>
        <ul>
          <li v-for="error in errors">{{ error }}</li>
        </ul>
      </p>
      <b-form inline>
        <b-form-input
        id="rule-number"
        v-model="rule_number"
        class="mb-2 mr-sm-2 mb-sm-0"
        placeholder="00100"
        ></b-form-input>
        <b-input
        id="rule-format"
        v-model="rule_format"
        class="mb-2 mr-sm-2 mb-sm-0"
        placeholder="allow"
        ></b-input>
        <b-input
        id="protocol"
        v-model="protocol"
        class="mb-2 mr-sm-2 mb-sm-0"
        placeholder="all"
        ></b-input>
        <b-card-text class="mb-2 mr-sm-2 mb-sm-0">From</b-card-text>
        <b-input
        id="from-target"
        v-model="from_target"
        class="mb-2 mr-sm-2 mb-sm-0"
        placeholder="any"
        ></b-input>
        <b-card-text class="mb-2 mr-sm-2 mb-sm-0">To</b-card-text>
        <b-input
        id="to-target"
        v-model="to_target"
        class="mb-2 mr-sm-2 mb-sm-0"
        placeholder="any"
        ></b-input>
      </b-form>
      <b-button class="mt-2" type="submit" variant="primary" @click="ipfw_exec">Submit</b-button>
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
            firewall_lists: [],
            rule_number: "",
            rule_format: "",
            protocol: "",
            from: "",
            from_target: "",
            to: "",
            to_target: "",
            errors: []
          }
        },
        components: {
            'vue-loading': VueLoading
        },
        methods: {
          ipfw_add() {
            this.$refs['add_button'].toggle('#ipfw-add')
          },
          ipfw_exec(e) {
            this.errors = [];
            if (!this.rule_number) {
              this.errors.push("Rule Number required.");
            }
            if (!this.rule_format) {
              this.errors.push("Rule Format required.");
            }
            if (!this.protocol) {
              this.errors.push("Protocol required.");
            }
            if (!this.from_target) {
              this.errors.push("Form Target required.");
            }
            if (!this.to_target) {
              this.errors.push("To Target required.");
            }
            if (this.errors.length) {
              e.preventDefault();
              return;
            }
            this.$store.state.loading = true
            axios.post(this.$store.state.serverName + '/firewall/add', {
              rule_number: this.rule_number,
              rule_format: this.rule_format,
              protocol:    this.protocol,
              from:        "from",
              from_target: this.from_target,
              to:          "to",
              to_target:   this.to_target
            }).then(response => {
              this.$store.dispatch('reload_jails')
              this.$store.state.loading = false
            }).catch(error => {
              this.$store.state.loading = false
              alert(error.response.data.reason)
            })
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