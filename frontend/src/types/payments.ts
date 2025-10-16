export type PaymentStatus = "Paid" | "Pending" | "Fail" 

export type Payment = {
  id: string;                
  amount: number;            
  currency: string;          
  status: PaymentStatus;     
  merchant: string;            
  timestamp: string;         
};

export type PaginatedPayments = {
    data: Payment[];
    total: number;
    limit: number;
    offset: number;
}
