import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface InvoicesState {
  page: number;
  limit: number;

  fromDate: string;
  toDate: string;
  status: string;

  setPage: (page: number) => void;
  setFromDate: (date: string) => void;
  setToDate: (date: string) => void;
  setStatus: (status: string) => void;
  resetFilters: () => void;
}

export const useInvoicesStore = create<InvoicesState>()(
  persist(
    (set) => ({
      page: 1,
      limit: 10,
      fromDate: '',
      toDate: '',
      status: '',

      setPage: (page) => set({ page }),
      setFromDate: (fromDate) => set({ fromDate, page: 1 }),
      setToDate: (toDate) => set({ toDate, page: 1 }),
       setStatus: (status) => set({ status, page: 1 }),
      resetFilters: () => set({ fromDate: '', toDate: '', status: '', page: 1 }),
    }),
    {
      name: 'invoices-storage', 
      partialize: (state) => ({
        page: state.page,
        fromDate: state.fromDate,
        toDate: state.toDate,
        status: state.status
      }),
    }
  )
);