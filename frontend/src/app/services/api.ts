import axios from "axios";
import { Payment } from "@/types/payments";

// Move to .env
const API_URL = "http://localhost:8000/api/payments/";

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
  const res = await axios.get<Payment[]>(API_URL, { params });
  return res.data;
}
