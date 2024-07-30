<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card">
          <div class="card-header">
            <h3>Payment Form</h3>
          </div>
          <div class="card-body">
            <form @submit.prevent="handleSubmit">
              <div class="form-group">
                <label for="cardNumber">Card Number</label>
                <input type="text" id="cardNumber" v-model="cardNumber" class="form-control" required />
              </div>
              <div class="form-group">
                <label for="cardName">Name on Card</label>
                <input type="text" id="cardName" v-model="cardName" class="form-control" required />
              </div>
              <div class="form-group">
                <label for="expiryDate">Expiry Date</label>
                <input type="text" id="expiryDate" v-model="expiryDate" class="form-control" required />
              </div>
              <div class="form-group">
                <label for="cvv">CVV</label>
                <input type="text" id="cvv" v-model="cvv" class="form-control" required />
              </div>
              <div class="form-group">
                <label for="amount">Amount</label>
                <input type="number" id="amount" v-model="amount" class="form-control" required />
              </div>
              <button type="submit" class="btn btn-primary">Submit Payment</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Swal from 'sweetalert2';

export default {
  data() {
    return {
      cardNumber: '',
      cardName: '',
      expiryDate: '',
      cvv: '',
      amount: ''
    };
  },
  methods: {
    async handleSubmit() {
      const result = await Swal.fire({
        title: 'Confirm Payment',
        text: "Do you want to proceed with the payment?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Yes, proceed!',
        cancelButtonText: 'No, cancel!'
      });

      if (result.isConfirmed) {
        try {
          // Simulate a payment processing request
          await new Promise(resolve => setTimeout(resolve, 2000)); // Simulate delay

          Swal.fire('Payment Successful!', 'Your payment has been processed.', 'success');

          // Navigate to the PDF display page
          this.$router.push('/view-pdf');

        } catch (error) {
          Swal.fire('Payment Failed!', 'There was an error processing your payment.', 'error');
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

.form-group {
  margin-bottom: 15px;
}

.form-control {
  padding: 10px;
  font-size: 16px;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
}

.btn-primary:hover {
  background-color: #0056b3;
  border-color: #004085;
}
</style>
