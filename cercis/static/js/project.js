var app = new Vue({
  el: "#navbarApp",
  delimiters: ['{$', '$}'],
  data: {},
  methods: {}
});

var app = new Vue({
  el: "#messagesApp",
  delimiters: ['{$', '$}'],
  data: {
    dismissSecs: 5,
    dismissCountDown: 0
  },
  methods: {
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown
    },
    showAlert() {
      this.dismissCountDown = this.dismissSecs
    }
  }
});