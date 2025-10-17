'use client';

import { useQuery } from '@tanstack/react-query';
import { Box, Container, Paper, Typography, Stack, Divider } from '@mui/material';
import { styled } from '@mui/material/styles';
import { AttachMoney, Receipt, CheckCircle, Error } from '@mui/icons-material';
import { fetchSummary } from './services/api';

const GridContainer = styled(Box)(({ theme }) => ({
  display: 'grid',
  gap: theme.spacing(3),
  gridTemplateColumns: 'repeat(4, 1fr)',
  '@media (max-width: 1200px)': {
    gridTemplateColumns: 'repeat(2, 1fr)',
  },
  '@media (max-width: 600px)': {
    gridTemplateColumns: '1fr',
  },
}));

const StatCard = ({ title, value, icon, color }: { title: string; value: string | number; icon: React.ReactNode; color: string }) => (
  <Paper
    sx={{
      p: 3,
      display: 'flex',
      alignItems: 'center',
      gap: 2,
      height: '100%'
    }}
    elevation={2}
  >
    <Box sx={{ color: color }}>{icon}</Box>
    <Box>
      <Typography variant="h6" component="div">
        {value}
      </Typography>
      <Typography color="text.secondary" variant="body2">
        {title}
      </Typography>
    </Box>
  </Paper>
);

export default function Home() {
  // Get data for the last 30 days
  const toDate = new Date().toISOString().split('T')[0];
  const fromDate = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000)
    .toISOString()
    .split('T')[0];

  const { data: summary, isLoading, isError } = useQuery({
    queryKey: ['summary', fromDate, toDate],
    queryFn: () => fetchSummary({ from_date: fromDate, to_date: toDate }),
  });

  // Compute counts for Paid vs Unpaid invoices from summary
  const paidInvoiceCount = summary?.paid_invoices_count ?? 0;
  const unpaidInvoiceCount = summary?.unpaid_invoices_count ?? 0;
  const maxInvoiceCount = Math.max(paidInvoiceCount, unpaidInvoiceCount, 1);

  if (isError || !summary) {
    return <Typography color="error">Failed to load dashboard data</Typography>;
  }

  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat('en-GB', {
      style: 'currency',
      currency: 'GBP'
    }).format(amount);
  };

  console.log(summary)

  return (
    <Container maxWidth="xl">
      <Box sx={{ p: 3 }}>
        <Typography variant="h4" gutterBottom>
          Dashboard Overview
        </Typography>
        <GridContainer>
          <StatCard
            title="Total Payments"
            value={formatCurrency(summary.total_payments_amount)}
            icon={<AttachMoney fontSize="large" />}
            color="#2196f3"
          />
          <StatCard
            title="Total Invoices"
            value={formatCurrency(summary.total_invoices_amount)}
            icon={<Receipt fontSize="large" />}
            color="#4caf50"
          />
          <StatCard
            title="Paid Invoices"
            value={formatCurrency(summary.paid_invoices_amount)}
            icon={<CheckCircle fontSize="large" />}
            color="#00c853"
          />
          <StatCard
            title="Unpaid Invoices"
            value={formatCurrency(summary.unpaid_invoices_amount)}
            icon={<Error fontSize="large" />}
            color="#f44336"
          />
          
          <StatCard
            title="Payment Count"
            value={summary.total_payments_count}
            icon={<AttachMoney fontSize="large" />}
            color="#2196f3"
          />
          <StatCard
            title="Invoice Count"
            value={summary.total_invoices_count}
            icon={<Receipt fontSize="large" />}
            color="#4caf50"
          />
          <StatCard
            title="Paid Invoice Count"
            value={summary.paid_invoices_count}
            icon={<CheckCircle fontSize="large" />}
            color="#00c853"
          />
          <StatCard
            title="Unpaid Invoice Count"
            value={summary.unpaid_invoices_count}
            icon={<Error fontSize="large" />}
            color="#f44336"
          />
        </GridContainer>

        {/* Paid vs Unpaid Invoices Bar Chart */}
        <Paper sx={{ mt: 3, p: 3 }} elevation={2}>
          <Typography variant="h6" gutterBottom>
            Paid vs Unpaid Invoices
          </Typography>
          <Stack direction="row" spacing={4} alignItems="end" sx={{ height: 160 }}>
            <Stack alignItems="center" spacing={1} sx={{ height: 1 }}>
              <Box sx={{ width: 64, height: `${(paidInvoiceCount / maxInvoiceCount) * 100}%`, backgroundColor: 'success.main', borderRadius: 1 }} />
              <Typography variant="body2">Paid</Typography>
              <Typography variant="caption" color="text.secondary">{paidInvoiceCount}</Typography>
            </Stack>
            <Stack alignItems="center" spacing={1} sx={{ height: 1 }}>
              <Box sx={{ width: 64, height: `${(unpaidInvoiceCount / maxInvoiceCount) * 100}%`, backgroundColor: 'warning.main', borderRadius: 1 }} />
              <Typography variant="body2">Unpaid</Typography>
              <Typography variant="caption" color="text.secondary">{unpaidInvoiceCount}</Typography>
            </Stack>
          </Stack>
          <Divider sx={{ mt: 2 }} />
        </Paper>
      </Box>
    </Container>
  );
}
