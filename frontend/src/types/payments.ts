type PaymentStatus = "Paid" | "Pending" | "Fail" 

type Payment = {
  id: string;                
  amount: number;            
  currency: string;          
  status: InvoiceStatus;     
  merchant: string;            
  timestamp: string;         
};
