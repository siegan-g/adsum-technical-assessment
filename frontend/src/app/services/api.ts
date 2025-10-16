import axios from "axios";
<<<<<<< Updated upstream
import { Payment } from "@/types/payments";
=======
import { Payment, PaymentResponse } from "@/types/payments";
import { InvoiceResponse } from "@/types/invoices";
>>>>>>> Stashed changes

// Move to .env
const API_URL = "http://localhost:8000/api";

export async function fetchPayments({
  limit,
  offset,
  from_date,
  to_date,
}: {
  limit: number;
  offset: number;
  from_date?: string;
  to_date?: string;
}): Promise<Payment[]> {
  const params: Record<string, string| number> = { limit, offset };
  if (from_date) params.from_date = from_date;
  if (to_date) params.to_date = to_date;
<<<<<<< Updated upstream
  const res = await axios.get<Payment[]>(API_URL, { params });
=======
  if (status) params.status = status;
  const res = await axios.get<PaymentResponse>(API_URL+"/payments", { params });
  console.log(res);
  return res.data;
}

export async function fetchInvoices({
  limit,
  offset,
  from_date,
  to_date,
  status,
}: {
  limit: number;
  offset: number;
  from_date?: string;
  to_date?: string;
  status?: string;
}): Promise<InvoiceResponse> {
  const params: Record<string, string | number> = { limit, offset };
  if (from_date) params.from_date = from_date;
  if (to_date) params.to_date = to_date;
  if (status) params.status = status;
  const res = await axios.get<InvoiceResponse>(API_URL+"/invoices", { params });
  console.log(res);
>>>>>>> Stashed changes
  return res.data;
}
