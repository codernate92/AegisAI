import { useEffect } from "react";
import { Box, Heading, VStack, Text, Spinner } from "@chakra-ui/react";
import useSWR from "swr";
import axios from "axios";

const fetcher = (url) => axios.get(url).then(res => res.data);

export default function Home() {
  const { data: iocs, error: iocError } = useSWR(
    `${process.env.API_BASE_URL}/iocs/latest`,
    fetcher
  );
  const { data: summaries, error: sumError } = useSWR(
    `${process.env.API_BASE_URL}/summaries`,
    fetcher
  );

  if (!iocs || !summaries) {
    return (
      <Box textAlign="center" py={10}>
        <Spinner size="xl" />
        <Text>Loading threat intel...</Text>
      </Box>
    );
  }

  return (
    <Box p={8}>
      <Heading mb={4}>AegisAI Threat Intel Dashboard</Heading>
      <VStack align="start" spacing={6}>
        <Box w="100%">
          <Heading size="md">Latest IOCs</Heading>
          {iocError ? <Text>Error loading IOCs</Text> :
            iocs.map((ioc) => (
              <Text key={ioc.value}>{ioc.value} ({ioc.ioc_type})</Text>
            ))
          }
        </Box>
        <Box w="100%">
          <Heading size="md">Recent Summaries</Heading>
          {sumError ? <Text>Error loading summaries</Text> :
            summaries.map((s) => (
              <Box key={s.created_at} p={4} bg="gray.50" borderRadius="md">
                <Text fontSize="sm" color="gray.500">{new Date(s.created_at).toLocaleString()}</Text>
                <Text mt={2}>{s.content}</Text>
              </Box>
            ))
          }
        </Box>
      </VStack>
    </Box>
  );
}
