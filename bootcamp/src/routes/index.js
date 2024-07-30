import { createRouter, createWebHistory } from 'vue-router'
import DashboardPage from '../components/DashboardPage.vue'
import LoginPage from '../components/LoginPage.vue'
import HelloWorld from '../components/HelloWorld.vue'
import SignUp from '../components/SignUp.vue'
import AdminLogin from '../components/AdminLogin.vue'
import AdminDashboard from '../components/AdminDashboard.vue'
import UserLogin from '../components/UserLogin.vue'
import AddSection from '../components/Section/AddSection.vue'
import AddBook from '../components/Books/AddBook.vue'
import ManageBooks from '../components/Books/ManageBooks.vue'
import StoringBooks from '../components/Books/StoringBooks.vue'
import UserSection from '../components/UserSection.vue'
import UserBooks from '../components/UserBooks.vue'
import UserProfile from '../components/UserProfile'
import UserBookAccess from '../components/UserBookAccess.vue'
// import PayementSs from '../components/PayementSs.vue'
import PdfViewer from '../components/PdfViewer.vue'
const routes = [
  {
    path: '/dashboard',
    name: "Dashboard",
    component: DashboardPage
  },
  {
    path: '/login',
    name: "login",
    component: LoginPage
  },
  {
    path: '/',
    name: "helloworld",
    component: HelloWorld
  },
  {
    path: '/signup',
    name: "signup",
    component: SignUp
  },
  {
    path: '/admin',
    name: "admin",
    component: AdminLogin
  },
  {
    path: '/adminDashboard',
    name: "adminDashboard",
    component: AdminDashboard,
    meta: { isAdmin: true }

  },
  {
    path: '/userlogin',
    name: "userlogin",
    component: UserLogin
  },
  {
    path: '/addsection',
    name: "addsection",
    component: AddSection
  },
  {
    path: '/addbook/:section_id',
    name: "addbook",
    component: AddBook
  },
  {
    path: '/managebook',
    name: "managebook",
    component: ManageBooks
  },
  {
    path: '/storebooks/:section_id',
    name: "storebooks",
    component: StoringBooks
  },
  {
    path: '/usersection/:user_id',
    // path: '/usersection',
    name: "usersection",
    component: UserSection
  },
  {
    path: '/userbooks/:user_id/:section_id',
    name: "userbooks",
    component: UserBooks
  },
  {
    path: '/profile/:user_id',
    // path: '/profile',
    name: 'Profile',
    component: UserProfile
  },
  {
    path : '/userbookaccess',
    name : 'UserBookAccess',
    component : UserBookAccess
  },
  // {
  //   path: '/payment/:bookId', // Updated to use :bookId for dynamic book ID
  //   name: 'Payment',
  //   component: PayementSs
  // },
  {
    path: '/view-pdf/:bookId',
    name: 'PdfViewer',
    component: PdfViewer
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const userRole = localStorage.getItem('userRole') || 'user';

  if (to.meta.isAdmin && userRole !== 'admin') {
    next({ path: '/login', query: { unauthorized: true } });
  } else {
    next();
  }
})

export default router;