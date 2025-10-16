export type InvoiceStatus = "Paid" | "Pending" | "Fail" 

export type Invoice = {
  id: string;                
  amount: number;            
  currency: string;          
  status: InvoiceStatus;     
  dueDate: string;           
  client: string;            
  timestamp: string;         
};
