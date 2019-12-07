<template>
  <div id="terminal"></div>
</template>

<script>
    import axios from 'axios'
    import { Terminal } from 'xterm';

    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    export default {
        name: 'Jails-Connect',
        mounted: function () {
          const term = new Terminal();
          term.open(document.getElementById('terminal'));
          term.write("$ ");
          term.onKey((data) => {
            if (data.domEvent.key === "Enter") {
              term.write("\r\n");
              term.write("$ ");
            } else {
              term.write(data.key);
            }
          });
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