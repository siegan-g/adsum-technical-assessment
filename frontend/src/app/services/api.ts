import axios from "axios";
import { Payment, PaymentResponse } from "@/types/payments";
import { InvoiceResponse } from "@/types/invoices";

// Move to .env
const API_URL = "http://localhost:8000/api";

export async function fetchPayments({
  limit,
  offset,
  from_date,
  to_date,
  status
}: {
  limit: number;
  offset: number;
  from_date?: string;
  to_date?: string;
  status?:string;
}): Promise<PaymentResponse> {
  const params: Record<string, string| number> = { limit, offset };
  if (from_date) params.from_date = from_date;
  if (to_date) params.to_date = to_date;
  if (status) params.status = status;
  const res = await axios.get<PaymentResponse>(API_URL+"/payments", { params });
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
  return res.data;
}
