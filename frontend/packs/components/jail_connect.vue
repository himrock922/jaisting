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
          let cursor = 0;
          term.onKey((data) => {
            switch(data.domEvent.key) {
              case "Enter":
                term.write("\r\n");
                term.write("$ ");
                cursor = 0;
                break;
              case "ArrowUp", "ArrowDown":
                break;
              case "ArrowLeft":
                if(cursor > 0) {
                  cursor -= 1;
                  term.write(data.key);
                }
                break;
              case "Backspace":
                if(cursor > 0) {
                  cursor -= 1;
                  term.write('\x1b[D');
                }
                break;
              default:
                if(cursor < 70) {
                  cursor += 1;
                  term.write(data.key);
                }
                break;
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