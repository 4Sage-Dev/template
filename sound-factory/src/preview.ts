// Sound Factory — Audio Registry and Playback Integration
// This file is used by player.html for sound preview.

// 1. THE SOUND MAP (Add new sounds here)
const soundMap: Record<string, string> = {
  example: '/sounds/example/sound.wav'
};

// 2. PLAYBACK
let currentAudio: HTMLAudioElement | null = null;

export function playSound(name: string): void {
  if (currentAudio) {
    currentAudio.pause();
    currentAudio = null;
  }

  const path = soundMap[name];
  if (!path) {
    console.error(`Sound not found: ${name}`);
    return;
  }

  currentAudio = new Audio(path);
  currentAudio.play().catch(e => console.error('Playback failed:', e));
  currentAudio.onended = () => { currentAudio = null; };
}

export function stopAll(): void {
  if (currentAudio) {
    currentAudio.pause();
    currentAudio = null;
  }
}

export { soundMap };
