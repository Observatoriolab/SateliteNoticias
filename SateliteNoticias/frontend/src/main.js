import Vue from "vue";
import App from "./App.vue";
import router from "./router";
Vue.config.productionTip = false;
import { BootstrapVue, BootstrapVueIcons } from "bootstrap-vue";
import { MdButton, MdContent, MdTabs, MdDrawer, MdToolbar, MdIcon, MdList } from 'vue-material/dist/components'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

Vue.use(MdButton)
Vue.use(MdContent)
Vue.use(MdTabs)
Vue.use(MdDrawer)
Vue.use(MdToolbar)
Vue.use(MdIcon)
Vue.use(MdList)

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
