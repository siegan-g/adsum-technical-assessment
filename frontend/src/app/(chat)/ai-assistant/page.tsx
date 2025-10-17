"use client";

import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { fetchAiAssistant } from "@/app/services/api";
import { useChatStore } from "@/stores/chatStore";
import {
  Container,
  Box,
  TextField,
  Button,
  Typography,
  Paper
} from "@mui/material";
import { v4 as uuid } from "uuid";

export default function ChatPage() {
  const [input, setInput] = useState("");
  const { messages, addMessage } = useChatStore();

  const mutation = useMutation({
    mutationFn: fetchAiAssistant,
    onSuccess: (data) => {
      addMessage({ id: uuid(), role: "assistant", content: data.message });
    }
  });

  const handleSend = () => {
    if (!input.trim()) return;
    addMessage({ id: uuid(), role: "user", content: input });
    mutation.mutate(input);
    setInput("");
  };

  return (
    <Container maxWidth="sm" sx={{ mt: 5 }}>
      <Typography variant="h5" mb={2}>
        Chat with LLM
      </Typography>

      <Paper variant="outlined" sx={{ p: 2, height: "60vh", overflowY: "auto" }}>
        {messages.map((msg) => (
          <Box
            key={msg.id}
            sx={{
              mb: 2,
              textAlign: msg.role === "user" ? "right" : "left"
            }}
          >
            <Typography
              sx={{
                display: "inline-block",
                p: 1.5,
                borderRadius: 2,
                bgcolor: msg.role === "user" ? "primary.main" : "grey.300",
                color: msg.role === "user" ? "white" : "black"
              }}
            >
              {msg.content}
            </Typography>
          </Box>
        ))}
      </Paper>

      <Box sx={{ display: "flex", mt: 2, gap: 1 }}>
        <TextField
          fullWidth
          placeholder="Type a message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <Button
          variant="contained"
          disabled={mutation.isPending}
          onClick={handleSend}
        >
          Send
        </Button>
      </Box>
    </Container>
  );
}