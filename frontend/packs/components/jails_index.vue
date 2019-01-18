<template>
  <table class="table table-striped table-sm">
    <thead>
    <tr>
      <th>JID</th>
      <th>NAME</th>
      <th>STATE</th>
      <th>RELEASE</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
    </thead>
    <tbody id="app">
    <tr v-for="jail in $store.state.jails" :key="jail.id">
      <td>{{ jail.jid }}</td>
      <td>{{ jail.name }}</td>
      <td>{{ jail.status }}</td>
      <td>{{ jail.release }}</td>
      <td><a :href="'/jails/' + jail.name" class="btn btn-info">Show</a></td>
      <td v-if="jail.status == 'up'">
        <jail-stop :jail_name=jail.name></jail-stop>
      </td>
      <td v-else>
        <jail-start :jail_name=jail.name></jail-start>
      </td>
      <td v-if="jail.status == 'down'">
        <jail-delete :jail_name=jail.name></jail-delete>
      </td>
    </tr>
    </tbody>
  </table>
</template>

<script>
    import axios from 'axios'
    import JailStart from './jail_start.vue'
    import JailStop from './jail_stop.vue'
    import JailDelete from './jail_delete.vue'

    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    export default {
        name: 'Jails-Index',
        components: {
            'jail-delete': JailDelete,
            'jail-start': JailStart,
            'jail-stop': JailStop,
        },
        created: function () {
            this.$store.dispatch('reload_jails')
        }
    }
</script>

<style scoped>

</style>