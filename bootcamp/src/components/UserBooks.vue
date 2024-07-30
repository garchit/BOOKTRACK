<!-- <template>
    <div>
        <h1>Books</h1>
        <div class="container">
            <div class="row">
                <div v-for="book in books" :key="book.id" class="col-md-4 mb-4">
                    <div class="card">
                        <img :src="book.poster" class="card-img-top" alt="Book Cover" height="300px" width="300px">
                        <div class="card-body">
                            <h5 class="card-title">{{ book.name }}</h5>
                            <p class="card-text">Author - {{ book.author }}</p>
                            <p class="card-text">Price - {{ book.price }}</p>
                            <a href="/payment" class="btn btn-primary mr-3">Download Book</a>
                            <button class="btn btn-primary"
                                @click="requestAccess(book.id, current_user, username, book.name)">Request
                                Access</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="books.length === 0">
            <p>No books available.</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            books: [],
            section_id: null // Initialize section_id
        };
    },
    mounted() {
        // Fetch section_id from route parameters
        this.section_id = this.$route.params.section_id;
        this.fetchBooks();
    },
    methods: {
        async fetchBooks() {
            try {
                const response = await axios.get(`/storebooks/${this.section_id}`);
                this.books = response.data;
            } catch (error) {
                console.error('Error fetching books:', error);
            }
        },
        formatDate(date) {
            return new Date(date).toLocaleDateString('en-US');
        },
    },
};
</script> -->



<template>
    <div>
        <h1>Books</h1>
        <div class="container">
            <div class="row">
                <div v-for="book in books" :key="book.id" class="col-md-4 mb-4">
                    <div class="card">
                        <img :src="book.poster" class="card-img-top" alt="Book Cover" height="300px" width="300px">
                        <div class="card-body">
                            <h5 class="card-title">{{ book.name }}</h5>
                            <p class="card-text">Author - {{ book.author }}</p>
                            <p class="card-text">Price - {{ book.price }}</p>
                            <!-- <a href="/payment" class="btn btn-primary mr-3">Download Book</a> -->
                            <!-- <a href="`/payment/${book.id}`" class="btn btn-primary mr-3">Download Book</a> -->
                            <button class="btn btn-primary" @click="requestAccess(book.id, book.name)">
                                Request Access
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="books.length === 0">
            <p>No books available.</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            books: [],
            section_id: null, // Initialize section_id
            user_id: null,
            username: null
        };
    },
    mounted() {
        // Fetch section_id from route parameters
        this.section_id = this.$route.params.section_id;
        this.user_id = localStorage.getItem('user_id');
        this.username = localStorage.getItem('username');
        console.log('User ID:', this.user_id);
        console.log('Username:', this.username);
        this.fetchBooks();
        this.fetchRequestedBooksCount();
    },
    methods: {
        async fetchBooks() {
            try {
                const response = await axios.get(`/storebooks/${this.section_id}`);
                this.books = response.data;
                console.log('Books fetched:', this.books);
            } catch (error) {
                console.error('Error fetching books:', error);
            }
        },
        async fetchRequestedBooksCount() {
            try {
                const response = await axios.get(`/api/requested-books-count`, {
                    params: { user_id: this.user_id }
                });
                this.requestedBooksCount = response.data.count;
                console.log('Requested books count:', this.requestedBooksCount);
            } catch (error) {
                console.error('Error fetching requested books count:', error);
            }
        },
        async requestAccess(bookId, bookName) {

            if (this.requestedBooksCount >= 5) {
                this.$swal.fire('Limit Exceeded', 'You cannot request more than 5 books at a time.', 'error');
                return;
            }

            console.log('Requesting access for book:', bookName, 'by user:', this.username);
            const { value: days } = await this.$swal.fire({
                title: 'For how many days do you want to take access?',
                input: 'number',
                inputAttributes: {
                    min: 1,
                    max: 7,
                    step: 1
                },
                inputValidator: (value) => {
                    if (!value || value < 1 || value > 7) {
                        return 'Invalid number of days. Please enter a number between 1 and 7.';
                    }
                },
                showCancelButton: true
            });

            if (!days) {
                console.log('Request canceled or invalid input');
                return; // Cancel button pressed or invalid input
            }

            console.log('Days selected:', days);

            const confirmation = await this.$swal.fire({
                title: 'Are you sure?',
                icon: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Yes, send request!',
                cancelButtonText: 'No, cancel!'
            });

            console.log('User ID:', this.user_id);
            console.log('Username:', this.username);
            console.log('Book ID:', bookId);
            console.log('Days:', days);
            console.log('Book Name:', bookName);

            if (confirmation.isConfirmed) {
                console.log('User confirmed the request');
                try {
                    const response = await axios.post('/api/request-access', {
                        section_id: this.section_id,
                        user_id: this.user_id,
                        book_id: bookId,
                        days: parseInt(days, 10),
                        book_name: bookName,
                        user_name: this.username
                    });

                    if (response.data.success) {
                        console.log('Request sent successfully');
                        this.$swal.fire('Success', 'Your request was sent successfully.', 'success');
                    } else {
                        console.log('Failed to send request:', response.data.message);
                        this.$swal.fire('Error', 'Failed to send request.', 'error');
                    }
                } catch (error) {
                    console.error('Error requesting access:', error);
                    this.$swal.fire('Error', 'An error occurred. Please try again.', 'error');
                }
            } else {
                console.log('User canceled the request');
            }
        }
    }
};
</script>
