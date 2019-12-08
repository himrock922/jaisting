<template>
  <div id="terminal"></div>
</template>

<script>
    import axios from 'axios'
    import { Terminal } from 'xterm';
    import { AttachAddon } from 'xterm-addon-attach';

    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFToken';

    const term = new Terminal();
    const socket = new WebSocket("ws://133.242.137.151:8080/" + window.location.pathname.slice(0, -8) + "/websocket");
    const attachAddon = new AttachAddon(socket);
    socket.addEventListener( "message", (response) => {
      term.write("$ " + response.data + "\r\n");
      term.write("$ ");
    });

    export default {
        name: 'Jails-Connect',
        mounted: function () {
          let current_line = "";
          const jail_name = document.getElementById("jail_name").value;
          term.open(document.getElementById('terminal'));
          term.write("$ ");
          let cursor = 0;
          term.onKey((data) => {
            switch(data.domEvent.key) {
              case "Enter":
                term.write("\r\n");
                if(current_line) {
                  socket.send(JSON.stringify({
                    'message': current_line,
                    "jail_name": jail_name
                  }));
                } else {
                  term.write("\r\n");
                  term.write("$ ");
                }
                cursor = 0;
                current_line = "";
                break;
              case "ArrowUp":
              case "ArrowDown":
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
                  current_line = current_line.slice(0, -1);
                  term.write('\b \b');
                }
                break;
              default:
                if (cursor < 120) {
                  cursor += 1;
                  current_line += data.key;
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