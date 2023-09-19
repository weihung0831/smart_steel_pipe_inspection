<script>
//  back to top
$(document).ready(function () {
  // 當頁面滾動時
  $(window).scroll(function () {
    // 如果頁面高度大於 300px，則顯示按鈕
    if ($(this).scrollTop() > 100) {
      $("#back-to-top").fadeIn();
    } else {
      $("#back-to-top").fadeOut();
    }
  });

  // 當按鈕被點擊時
  $("#back-to-top").click(function () {
    // 平滑滾動到頁面頂部
    $("html, body").animate({ scrollTop: 0 }, 10);
    return false;
  });
});
</script>

<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav navbar-center">
          <li class="nav-item active">
            <a class="nav-link" href="#page1">測量顯示</a>
          </li>
          <li class="nav-item active">
            <a class="nav-link" href="#page2">動作設定</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#page3">測量設定</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#page4">I/O狀態</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#page5">異常紀錄</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#page6">資料保存</a>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>
