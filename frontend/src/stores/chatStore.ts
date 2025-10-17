import { create } from "zustand";
import { persist, createJSONStorage } from "zustand/middleware";

export type ChatMessage = {
  id: string;
  role: "user" | "assistant";
  content: string;
};

type ChatStore = {
  messages: ChatMessage[];
  addMessage: (msg: ChatMessage) => void;
  clearChat: () => void;
};

export const useChatStore = create<ChatStore>()(
  persist(
    (set) => ({
      messages: [],
      addMessage: (msg) =>
        set((state) => ({ messages: [...state.messages, msg] })),
      clearChat: () => set({ messages: [] })
    }),
    {
      name: "chat-store",
      storage: createJSONStorage(() => localStorage)
    }
  )
);
