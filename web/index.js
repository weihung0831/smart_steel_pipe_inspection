const { createApp } = Vue;

const app = createApp({
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

//  back to top
$(document).ready(function(){
  // 當頁面滾動時
  $(window).scroll(function(){
      // 如果頁面高度大於 300px，則顯示按鈕
      if ($(this).scrollTop() > 100) {
          $('#back-to-top').fadeIn();
      } else {
          $('#back-to-top').fadeOut();
      }
  });

  // 當按鈕被點擊時
  $('#back-to-top').click(function(){
      // 平滑滾動到頁面頂部
      $('html, body').animate({scrollTop : 0}, 50);
      return false;
  });
});
