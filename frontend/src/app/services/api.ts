import axios from "axios";
import { PaginatedPayments } from "@/types/payments";

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
}): Promise<PaginatedPayments> {
  const res = await axios.get(API_URL, {
    params: { limit, offset, from_date, to_date },
  });
  return res.data;
}
