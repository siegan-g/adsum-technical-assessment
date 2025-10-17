"use client";

import { useQuery } from "@tanstack/react-query";
import { fetchAgentLogs } from "@/app/services/api";
import { AgentLogs } from "@/types/agent-logs";
import { useAgentLogsStore } from "@/stores/agentLogsStore";
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

export default function AgentLogsPage() {
  // Get state and actions from Zustand store
  const { page, limit, fromDate, toDate, level, setPage, setFromDate, setToDate, setLevel, resetFilters } = useAgentLogsStore();

  const { data, isLoading, isError } = useQuery({
    queryKey: ["agent-logs", page, fromDate, toDate, level],
    queryFn: () =>
      fetchAgentLogs({
        limit,
        offset: (page - 1) * limit,
        from_date: fromDate,
        to_date: toDate,
        level: level
      }),
  });
  const totalPages = Math.ceil((data?.count ?? 0) / limit);

  return (
    <Paper sx={{ p: 2, m: 2 }}>
      <Typography variant="h6" noWrap sx={{ my: 2 }}>
        Agent Logs
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
          <InputLabel>Level</InputLabel>
          <Select
            value={level}
            label="Level"
            onChange={(e) => setLevel(e.target.value)}
          >
            <MenuItem value="">All</MenuItem>
            <MenuItem value="DEBUG">DEBUG</MenuItem>
            <MenuItem value="INFO">INFO</MenuItem>
            <MenuItem value="WARNING">WARNING</MenuItem>
            <MenuItem value="ERROR">ERROR</MenuItem>
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
                  <TableCell>Level</TableCell>
                  <TableCell>Message</TableCell>
                  <TableCell>Timestamp</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {data?.logs?.map((log: AgentLogs) => (
                    <TableRow key={log.id}>
                      <TableCell>{log.level}</TableCell>
                      <TableCell>{log.message}</TableCell>
                      <TableCell>{new Date(log.timestamp).toLocaleString()}</TableCell>
                    </TableRow>
                  ))
                }
 
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