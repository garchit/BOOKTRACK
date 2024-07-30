<!-- <template>
    <div class="container mt-5">
      <div class="row justify-content-center">
        <div class="col-md-10">
          <div class="card">
            <div class="card-header">
              <h3>User Book Access</h3>
            </div>
            <div class="card-body">
              <table class="table table-bordered">
                <thead>
                  <tr>
                    <th>Username</th>
                    <th>Book Name</th>
                    <th>User ID</th>
                    <th>Book ID</th>
                    <th>Days</th>
                    <th>Status</th>
                    <th>Options</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(access, index) in userBookAccessData" :key="index">
                    <td>{{ access.username }}</td>
                    <td>{{ access.book_name }}</td>
                    <td>{{ access.user_id }}</td>
                    <td>{{ access.bookId }}</td>
                    <td>{{ access.days }}</td>
                    <td>{{ access.status}}</td>
                    <td>
                        <button class="btn btn-success mr-3">Accept</button>
                        <button class="btn btn-danger">Decline</button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
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
        userBookAccessData: []
      };
    },
    mounted() {
      this.fetchUserBookAccessData();
    },
    methods: {
      async fetchUserBookAccessData() {
        try {
          const response = await axios.get('/api/user-access-data');
          this.userBookAccessData = response.data;
          console.log('User book access data:', this.userBookAccessData);
        } catch (error) {
          console.error('Error fetching user book access data:', error);
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
  </style>
   -->



   <template>
    <div class="container mt-5">
      <div class="row justify-content-center">
        <div class="col-md-10">
          <div class="card">
            <div class="card-header">
              <h3>User Book Access</h3>
            </div>
            <div class="card-body">
              <table class="table table-bordered">
                <thead>
                  <tr>
                    <th>Username</th>
                    <th>Book Name</th>
                    <th>User ID</th>
                    <th>Book ID</th>
                    <th>Days</th>
                    <th>Status</th>
                    <th>Options</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(access, index) in userBookAccessData" :key="index">
                    <td>{{ access.username }}</td>
                    <td>{{ access.book_name }}</td>
                    <td>{{ access.user_id }}</td>
                    <td>{{ access.bookId }}</td>
                    <td>{{ access.days }}</td>
                    <td>{{ access.status }}</td>
                    <td>
                      <button class="btn btn-success mr-3" @click="handleAccept(index, access.id)">Accept</button>
                      <button class="btn btn-danger" @click="handleDecline(index, access.id)">Decline</button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
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
        userBookAccessData: []
      };
    },
    mounted() {
      this.fetchUserBookAccessData();
    },
    methods: {
      async fetchUserBookAccessData() {
        try {
          const response = await axios.get('/api/user-access-data');
          this.userBookAccessData = response.data;
          console.log('User book access data:', this.userBookAccessData);
        } catch (error) {
          console.error('Error fetching user book access data:', error);
        }
      },
      async handleAccept(index, id) {
        const result = await Swal.fire({
          title: 'Are you sure?',
          text: "Do you want to grant access?",
          icon: 'warning',
          showCancelButton: true,
          confirmButtonText: 'Yes, grant it!',
          cancelButtonText: 'No, cancel!'
        });
  
        if (result.isConfirmed) {
          try {
            await axios.post(`/api/update-access-status/${id}`, { status: 'Granted' });
            this.userBookAccessData[index].status = 'Granted';
            Swal.fire('Granted!', 'The access has been granted.', 'success');
          } catch (error) {
            console.error('Error updating status:', error);
            Swal.fire('Error!', 'Failed to update status.', 'error');
          }
        }
      },
      async handleDecline(index, id) {
        const result = await Swal.fire({
          title: 'Are you sure?',
          text: "Do you want to revoke access?",
          icon: 'warning',
          showCancelButton: true,
          confirmButtonText: 'Yes, revoke it!',
          cancelButtonText: 'No, cancel!'
        });
  
        if (result.isConfirmed) {
          try {
            await axios.post(`/api/update-access-status/${id}`, { status: 'Revoked' });
            this.userBookAccessData[index].status = 'Revoked';
            Swal.fire('Revoked!', 'The access has been revoked.', 'success');
          } catch (error) {
            console.error('Error updating status:', error);
            Swal.fire('Error!', 'Failed to update status.', 'error');
          }
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
  </style>
  