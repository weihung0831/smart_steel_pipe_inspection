import { createApp } from "vue";
import "../css/style.css";
import nav from "../vue/nav.vue";
import page1 from "../vue/page1.vue";
import page2 from "../vue/page2.vue";
import page3 from "../vue/page3.vue";
import page4 from "../vue/page4.vue";
import page5 from "../vue/page5.vue";
import page6 from "../vue/page6.vue";

createApp(nav).mount("#nav");
createApp(page1).mount("#page1");
createApp(page2).mount("#page2");
createApp(page3).mount("#page3");
createApp(page4).mount("#page4");
createApp(page5).mount("#page5");
createApp(page6).mount("#page6");
