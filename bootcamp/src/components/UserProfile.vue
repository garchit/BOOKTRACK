<!-- <template>
    <div class="container mt-5">
      <div class="row justify-content-center">
        <div class="col-md-8">
          <div class="card">
            <div class="card-header">
              <h3>User Profile</h3>
            </div>
            <div class="card-body">
              <form>
                <div class="form-group">
                  <label for="username">Username</label>
                  <input type="text" id="username" v-model="username" class="form-control" disabled />
                </div>
                <div class="form-group">
                  <label for="password">Password</label>
                  <input type="text" id="password" v-model="password" class="form-control" disabled />
                </div>
              </form>
            </div>
          </div>
  
          
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: localStorage.getItem('username') || 'Guest',
        password: '********' // You typically won't show the actual password
      }
    }
  }
  </script>
  
  <style scoped>
  .card {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .card-header {
    background-color: #f8f9fa;
    border-bottom: 1px solid #e9ecef;
  }
  
  .table {
    margin-top: 20px;
  }
  
  .table thead {
    background-color: #f8f9fa;
  }
  </style>
  

 -->

<!-- 
 <template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div class="card">
          <div class="card-header">
            <h3>User Profile</h3>
          </div>
          <div class="card-body">
            <form>
              <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" v-model="username" class="form-control" disabled />
              </div>
              <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" v-model="password" class="form-control" disabled />
              </div>
            </form>
          </div>
        </div>

        <div v-if="filteredAccessData.length > 0">
          <table class="table table-bordered mt-4">
            <thead>
              <tr>
                <th>Book Name</th>
                <th>Days</th>
                <th>Status</th>
                <th>Id of book</th>
                <th>Link</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(access, index) in filteredAccessData" :key="index">
                <td>{{ access.book_name }}</td>

                <td>{{ access.days }}</td>
                <td>{{ access.status}}</td>
                <td>{{access.bookId}}</td>
                 <td><a @click="handleLinkClick(access.bookId)" :href="`/view-pdf/${access.bookId}`">open url</a></td>
              </tr>
            </tbody>
          </table>
        </div>

        <div v-else>
          <p>No BOOK BORROWED</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: localStorage.getItem('username') || 'Guest',
      password: '********', // You typically won't show the actual password
      userAccessData: [],
      filteredAccessData: []
    };
  },
  mounted() {
    this.fetchUserAccessData();
  },
  methods: {
    async fetchUserAccessData() {
      try {
        const user_id = localStorage.getItem('user_id');
        console.log(user_id);

        const response = await axios.get('/api/user-access-data', {
          headers: {
            'user_id': user_id
          }
        });

        this.userAccessData = response.data;
        console.log('User access data:', this.userAccessData);

        this.filteredAccessData = this.userAccessData.filter(access => access.user_id == user_id);
        console.log(this.filteredAccessData)
      } catch (error) {
        console.error('Error fetching user access data:', error);
      }
    },
   
    handleLinkClick(access) {
      if (access.status === 'granted') {
        localStorage.setItem('bookId', access.bookId);
        this.$router.push(`/view-pdf/${access.bookId}`);
      } else {
        alert('Access not granted for this book.');
      }
    }
  }
};
</script>

<style scoped>
.card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card-header {
  background-color: #f8f9fa;
  border-bottom: 1px solid #e9ecef;
}

.table {
  margin-top: 20px;
}

.table th,
.table td {
  padding: 8px;
  text-align: left;
}

.table th {
  background-color: #f8f9fa;
}
</style> -->


<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div class="card">
          <div class="card-header">
            <h3>User Profile</h3>
          </div>
          <div class="card-body">
            <form>
              <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" v-model="username" class="form-control" disabled />
              </div>
              <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" v-model="password" class="form-control" disabled />
              </div>
            </form>
          </div>
        </div>

        <div v-if="filteredAccessData.length > 0">
          <table class="table table-bordered mt-4">
            <thead>
              <tr>
                <th>Book Name</th>
                <th>Days</th>
                <th>Status</th>
                <th>Id of book</th>
                <th>Link</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(access, index) in filteredAccessData" :key="index">
                <td>{{ access.book_name }}</td>
                <td>{{ access.days }}</td>
                <td>{{ access.status }}</td>
                <td>{{ access.bookId }}</td>
                <td>
                  <a @click="handleLinkClick($event, access)" href="#">open url</a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <div v-else>
          <p>No BOOK BORROWED</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Swal from 'sweetalert2';

export default {
  data() {
    return {
      username: localStorage.getItem('username') || 'Guest',
      password: '********', // You typically won't show the actual password
      userAccessData: [],
      filteredAccessData: []
    };
  },
  mounted() {
    this.fetchUserAccessData();
  },
  methods: {
    async fetchUserAccessData() {
      try {
        const user_id = localStorage.getItem('user_id');
        console.log(user_id);

        const response = await axios.get('/api/user-access-data', {
          headers: {
            'user_id': user_id
          }
        });

        this.userAccessData = response.data;
        console.log('User access data:', this.userAccessData);

        // Filter data based on user_id
        this.filteredAccessData = this.userAccessData.filter(access => access.user_id == user_id);
      } catch (error) {
        console.error('Error fetching user access data:', error);
        Swal.fire('Error', 'Failed to fetch user access data.', 'error');
      }
    },
    handleLinkClick(event, access) {
      if (access.status !== 'Granted') {
        event.preventDefault();
        Swal.fire('Access Denied', 'Access not granted for this book.', 'error');
        return;
      }
      
      localStorage.setItem('bookId', access.bookId);
      this.$router.push(`/view-pdf/${access.bookId}`);
    }
  }
};
</script>

<style scoped>
.card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card-header {
  background-color: #f8f9fa;
  border-bottom: 1px solid #e9ecef;
}

.table {
  margin-top: 20px;
}

.table th,
.table td {
  padding: 8px;
  text-align: left;
}

.table th {
  background-color: #f8f9fa;
}
</style>
