"use client";

import { useQuery } from "@tanstack/react-query";
import { fetchInvoices, fetchPayments } from "@/app/services/api";
import { Invoice } from "@/types/invoices";
import { useInvoicesStore } from "@/stores/invoicesStore";
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

export default function InvoicesPage() {
  // Get state and actions from Zustand store
  const { page, limit, fromDate, toDate, status, setPage, setFromDate, setToDate, setStatus, resetFilters } = useInvoicesStore();

  const { data, isLoading, isError } = useQuery({
    queryKey: ["invoices", page, fromDate, toDate, status],
    queryFn: () =>
      fetchInvoices({
        limit,
        offset: (page - 1) * limit,
        from_date: fromDate,
        to_date: toDate,
        status: status 
      }),
  });
  const totalPages = Math.ceil((data?.count ?? 0) / limit);

  return (
    <Paper sx={{ p: 2, m: 2 }}>
      <Typography variant="h6" noWrap sx={{ my: 2 }}>
       Invoices 
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
                  <TableCell>Due Date</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {data?.invoices?.map((invoice: Invoice) => (
                  <TableRow key={invoice.id}>
                    <TableCell>{invoice.currency}</TableCell>
                    <TableCell>{invoice.amount}</TableCell>
                    <TableCell>{invoice.status}</TableCell>
                    <TableCell>{invoice.client}</TableCell>
                    <TableCell>{new Date(invoice.timestamp).toLocaleString()}</TableCell>
                    <TableCell>{new Date(invoice.due_date).toLocaleString()}</TableCell>
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