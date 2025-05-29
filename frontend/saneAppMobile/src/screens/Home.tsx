import React, { useState } from 'react';
import { View, Text, Pressable, Image, StyleSheet, ActivityIndicator, Alert } from 'react-native';
import * as DocumentPicker from 'expo-document-picker';
import axios from 'axios';
import styles from '../assets/styles/homeStyles';
import { Video, ResizeMode } from 'expo-av';

export default function Home(): React.JSX.Element {
  const [selected, setSelected] = useState<'Home' | 'Estatísticas' | 'Arquivos'>('Home');
  const [uploading, setUploading] = useState(false);
  const [videoReady, setVideoReady] = useState(false);

  const handleFilePick = async () => {
    try {
      const result = await DocumentPicker.getDocumentAsync({
        type: ['text/csv', 'application/vnd.ms-excel', '*/*'], // aceita mais tipos pra aumentar compatibilidade
        copyToCacheDirectory: true,
      });

      if (!result.canceled && result.assets && result.assets.length > 0) {
        const file = result.assets[0];

        if (!file.name.toLowerCase().endsWith('.csv')) {
          Alert.alert('Arquivo inválido', 'Por favor, selecione um arquivo com extensão .csv');
          return;
        }

        const uri = file.uri;
        const fileName = file.name;

        const formData = new FormData();
        formData.append('file', {
          uri,
          type: 'text/csv',
          name: fileName,
        } as any);

        setUploading(true);
        setVideoReady(false);

        await axios.post('http://192.168.15.10:5000/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        setUploading(false);
        setVideoReady(true);
      }
    } catch (err) {
      console.error('Erro ao enviar arquivo:', err);
      Alert.alert('Erro', 'Falha ao enviar arquivo. Tente novamente.');
      setUploading(false);
    }
  };

  return (
    <View style={styles.container}>
      {/* Toolbar */}
      <View style={styles.toolbar}>
        <Pressable onPress={() => console.log('Perfil do usuário')}>
          <Image source={require('../assets/img/user-icon.png')} style={styles.userIcon} />
        </Pressable>

        <View style={styles.menu}>
          {['Home', 'Estatísticas', 'Arquivos'].map((item) => (
            <Pressable key={item} onPress={() => setSelected(item as any)} style={styles.menuItemWrapper}>
              <Text style={[styles.menuItem, selected === item && styles.menuItemSelected]}>
                {item}
              </Text>
              {selected === item && <View style={styles.underline} />}
            </Pressable>
          ))}
        </View>
      </View>

      {/* Conteúdo */}
      <View style={styles.uploadContainer}>
        <Text style={styles.uploadTitle}>ENVIE O SEU ARQUIVO CSV</Text>

        <Pressable style={styles.uploadButton} onPress={handleFilePick}>
          <Text style={styles.uploadButtonText}>Selecionar Arquivo</Text>
        </Pressable>

        {uploading && <ActivityIndicator size="large" color="#0000ff" />}

        {videoReady && (
          <Video
            source={{ uri: 'http://192.168.15.10:5000/video' }}
            useNativeControls
            resizeMode={ResizeMode.CONTAIN}
            style={{ width: '100%', height: 300, marginTop: 20 }}
          />
        )}
      </View>
    </View>
  );
}
