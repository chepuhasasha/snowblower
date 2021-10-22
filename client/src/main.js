import Vue from 'vue'

import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import Flex from '@/components/utils/Flex.vue'
import store from './store'
import router from './router'
import App from './App.vue'

library.add(fas);
library.add(fab);

Vue.component("icon", FontAwesomeIcon);
Vue.component("Flex", Flex);
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
