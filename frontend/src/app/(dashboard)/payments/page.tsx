"use client";

import { useQuery } from "@tanstack/react-query";
import { fetchPayments } from "@/app/services/api";
import { Payment } from "@/types/payments";
import { usePaymentsStore } from "@/stores/paymentsStore";
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Pagination,
  TextField,
  Button,
  Stack,
  Typography,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
} from "@mui/material";

export default function PaymentsPage() {
  // Get state and actions from Zustand store
  const { page, limit, fromDate, toDate, status, setPage, setFromDate, setToDate, setStatus, resetFilters } = usePaymentsStore();

  const { data, isLoading, isError } = useQuery({
    queryKey: ["payments", page, fromDate, toDate, status],
    queryFn: () =>
      fetchPayments({
        limit,
        offset: (page - 1) * limit,
        from_date: fromDate,
        to_date: toDate,
        status: status
      })
  });
  const totalPages = Math.ceil((data?.count ?? 0) / limit);

  return (
    <Paper sx={{ p: 2, m: 2 }}>
      <Typography variant="h6" noWrap sx={{ my: 2 }}>
        Payments 
      </Typography>
      <Stack direction="row" spacing={2} sx={{ mb: 2 }}>
        <TextField
          type="date"
          label="From Date"
          slotProps={{ inputLabel: { shrink: true } }}
          value={fromDate}
          onChange={(e) => setFromDate(e.target.value)}
        />

        <TextField
          type="date"
          label="To Date"
          slotProps={{ inputLabel: { shrink: true } }}
          value={toDate}
          onChange={(e) => setToDate(e.target.value)}
        />
        <FormControl sx={{ minWidth: 120 }}>
          <InputLabel>Status</InputLabel>
          <Select
            value={status}
            label="Status"
            onChange={(e) => setStatus(e.target.value)}
          >
            <MenuItem value="">All</MenuItem>
            <MenuItem value="Paid">Paid</MenuItem>
            <MenuItem value="Pending">Pending</MenuItem>
            <MenuItem value="Fail">Fail</MenuItem>
          </Select>
        </FormControl>
        <Button variant="outlined" onClick={resetFilters}>
          Clear Filters
        </Button>
      </Stack>

      {isLoading ? (
        <p>Loading Table</p>
      ) : isError ? (
        <p>Error fetching Table</p>
      ) : (
        <>
          <TableContainer component={Paper}>
            <Table>
              <TableHead>
                <TableRow>
                  <TableCell>Currency</TableCell>
                  <TableCell>Amount</TableCell>
                  <TableCell>Status</TableCell>
                  <TableCell>Merchant</TableCell>
                  <TableCell>Create Date</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {data?.payments?.map((payment: Payment) => (
                  <TableRow key={payment.id}>
                    <TableCell>{payment.currency}</TableCell>
                    <TableCell>{payment.amount}</TableCell>
                    <TableCell>{payment.status}</TableCell>
                    <TableCell>{payment.merchant}</TableCell>
                    <TableCell>{new Date(payment.timestamp).toLocaleString()}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
          <Pagination
            count={totalPages}
            page={page}
            onChange={(_, value) => setPage(value)}
            color="primary"
            sx={{ mt: 2 }}
          />
        </>
      )}
    </Paper>
  );
}