import { createApp } from 'vue'
import App from './App.vue'
import router from './routes'
import axios from 'axios'
// import Notifications from 'vue-notification';
import Toast from 'vue-toastification';
import 'vue-toastification/dist/index.css';

import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

// import Vuetify from 'vuetify';
// import 'vuetify/dist/vuetify.min.css';

// PDF Embed Library
// import Pdf from 'vue-pdf-embed';

// Import Vuelidate and its validators
import { VuelidatePlugin } from '@vuelidate/core';
import '@vuelidate/validators';

axios.defaults.baseURL = 'http://127.0.0.1:5000'

const instance = axios.create({
    baseURL: 'http://127.0.0.1:5000',

   
   
  });
  // Add a request interceptor to include user_id in headers


// createApp(App).use(router).mount('#app')
const app = createApp(App);
app.use(router)
// app.use(Notifications);
// app.use(Vuetify)
app.use(VueSweetalert2);
app.use(Toast);
// Use Vuelidate plugin
app.use(VuelidatePlugin);
// app.component('PdfViewerComponent', Pdf);
app.config.globalProperties.$axios = instance
app.mount('#app')
