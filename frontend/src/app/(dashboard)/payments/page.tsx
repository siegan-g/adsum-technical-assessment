"use client";

import { useState } from "react";
import { useQuery } from "@tanstack/react-query";
import { fetchPayments } from "@/app/services/api";
import { Payment } from "@/types/payments";
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
} from "@mui/material";

export default function PaymentsPage() {
  const [page, setPage] = useState(1);
  const [limit] = useState(10);
  const [fromDate, setFromDate] = useState("");
  const [toDate, setToDate] = useState("");

  const { data, isLoading, isError, refetch } = useQuery({
    queryKey: ["payments", page, fromDate, toDate],
    queryFn: () =>
      fetchPayments({
        limit,
        offset: (page - 1) * limit,
        from_date: fromDate,
        to_date: toDate,
      }),
  });
  return (
    <Paper sx={{ p: 2, m: 2 }}>
      <Typography variant="h6" noWrap sx={{my:2}}>
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
        <Button variant="contained" onClick={() => refetch()}>
          Filter
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
						<TableCell>ID</TableCell>
						<TableCell>Amount</TableCell>
						<TableCell>Currency</TableCell>
						<TableCell>Status</TableCell>
						<TableCell>Merchant</TableCell>
						<TableCell>Timestamp</TableCell>
					</TableRow>
				</TableHead>
				<TableBody>
					{data?.data?.map((payment:Payment)=>(
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

        </>
      )}
    </Paper>
  );
}
