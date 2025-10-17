export type PaymentStatus = "Paid" | "Pending" | "Fail" 

export type Payment = {
  id: string;                
  amount: number;            
  currency: string;          
  status: PaymentStatus;     
  merchant: string;            
  timestamp: string;         
};


export type PaymentPaginate = {
  limit: number;
  offset: number;
}

export type PaymentFilter = {
  fromDate: Date
  toDate: Date
  status: string
}

export type PaymentResponse = {
  payments: Payment[]
  paymentssFilter: PaymentFilter 
  paymentsPaginate: PaymentPaginate 
  count: number
}