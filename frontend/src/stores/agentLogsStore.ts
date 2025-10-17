import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface AgentLogsState {
    page: number;
    limit: number;

    fromDate: string;
    toDate: string;
    level: string;

    setPage: (page: number) => void;
    setFromDate: (date: string) => void;
    setToDate: (date: string) => void;
    setLevel: (level: string) => void;
    resetFilters: () => void;
}

export const useAgentLogsStore = create<AgentLogsState>()(
    persist(
        (set) => ({
            page: 1,
            limit: 10,
            fromDate: '',
            toDate: '',
            level: '',

            setPage: (page) => set({ page }),
            setFromDate: (fromDate) => set({ fromDate, page: 1 }),
            setToDate: (toDate) => set({ toDate, page: 1 }),
            setLevel: (level) => set({ level, page: 1 }),
            resetFilters: () => set({ fromDate: '', toDate: '', level: '', page: 1 }),
        }),
        {
            name: 'agent-logs-storage',
            partialize: (state) => ({
                page: state.page,
                fromDate: state.fromDate,
                toDate: state.toDate,
                level: state.level
            }),
        }
    )
);