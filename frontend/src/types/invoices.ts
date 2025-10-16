export type InvoiceStatus = "Paid" | "Pending" | "Fail" 

export type Invoice = {
  id: string;                
  amount: number;            
  currency: string;          
  status: InvoiceStatus;     
  due_date: Date;           
  client: string;            
  timestamp: string;         
};

export type InvoicePaginate = {
  limit: number;
  offset: number;
}

export type InvoiceFilter = {
  fromDate: Date
  toDate: Date
  status: string
}

export type InvoiceResponse = {
  invoices: Invoice[]
  invoicesFilter: Invoice 
  invoicesPaginate:InvoicePaginate 
  count: number
}
