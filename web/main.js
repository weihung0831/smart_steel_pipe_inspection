const app = Vue.createApp({
  data() {
    return {
      message: "",
    };
  },
  methods: {
    async say_hello() {
      this.message = await eel.say_something("ok")();
    },
  },
});

app.mount("#app");
